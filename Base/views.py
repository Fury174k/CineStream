from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Comment, Room, Celebrity, Watchlist
import requests
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here
def homepage(request):
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    placeholder_image = '/static/Images/placeholders/image_placeholder.png'

    try:
        # Fetch top three most popular movies
        response = requests.get(base_url.format('popular', api_key))
        data = response.json().get('results', [])[:3]

        popular_movies = [
            {
                'id': movie.get('id'),
                'title': movie.get('title'),
                'overview': movie.get('overview'),
                'release_date': movie.get('release_date'),
                'poster_url': f"https://image.tmdb.org/t/p/original{movie.get('poster_path')}" if movie.get('poster_path') else placeholder_image,
                'backdrop_url': f"https://image.tmdb.org/t/p/original{movie.get('backdrop_path')}" if movie.get('backdrop_path') else placeholder_image,
                'likes': movie.get('vote_count'),
                'genres': [genre['name'] for genre in movie.get('genres', [])]
            }
            for movie in data
        ]

        # Fetch additional movies data
        additional_movie_ids = [1203329, 822119, 799766]
        additional_movies = []
        for movie_id in additional_movie_ids:
            response = requests.get(base_url.format(movie_id, api_key))
            data = response.json()

            movie = {
                'id': movie_id,
                'title': data.get('title'),
                'overview': data.get('overview'),
                'release_date': data.get('release_date'),
                'poster_url': f"https://image.tmdb.org/t/p/original{data.get('poster_path')}" if data.get('poster_path') else placeholder_image,
                'backdrop_url': f"https://image.tmdb.org/t/p/original{data.get('backdrop_path')}" if data.get('backdrop_path') else placeholder_image,
                'likes': data.get('vote_count'),
                'genres': [genre['name'] for genre in data.get('genres', [])]
            }

            additional_movies.append(movie)

        # Fetch celebrity data
        celebrity_url = f'https://api.themoviedb.org/3/person/popular?api_key={api_key}'
        celebrity_response = requests.get(celebrity_url)
        celebrity_data = celebrity_response.json().get('results', [])

        celebrities = [
            {
                'id': celeb.get('id'),
                'name': celeb.get('name'),
                'profile_picture_url': f"https://image.tmdb.org/t/p/original{celeb.get('profile_path')}" if celeb.get('profile_path') else placeholder_image,
                'biography': celeb.get('biography', 'Biography not available.'),
                'birth_date': celeb.get('birthday'),
                'popularity': celeb.get('popularity')
            }
            for celeb in celebrity_data
        ]

        # Fetch watchlist for the authenticated user
        watchlist = []
        if request.user.is_authenticated:
            watchlist_entries = Watchlist.objects.filter(user=request.user)
            for entry in watchlist_entries:
                response = requests.get(base_url.format(entry.movie_id, api_key))
                data = response.json()
                movie = {
                    'id': entry.movie_id,
                    'title': data.get('title'),
                    'poster_url': f"https://image.tmdb.org/t/p/original{data.get('poster_path')}" if data.get('poster_path') else placeholder_image,
                    'release_date': data.get('release_date'),
                    'likes': data.get('vote_count')
                }
                watchlist.append(movie)

        top_movies = get_top_movies()
        top_genre = get_popular_genres() 
        top_box_office = get_top_box_office_movies()
        upcoming_movies = get_upcoming_movies()
        top_news = get_top_news()

        context = {
            'popular_movies': popular_movies,
            'additional_movies': additional_movies,
            'celebrities': celebrities,
            'watchlist': watchlist,
            'top_movies': top_movies,
            'top_genre': top_genre,
            'top_box_office': top_box_office,
            'upcoming_movies': upcoming_movies,
            'top_news': top_news,
        }

        return render(request, 'home.html', context)
    except requests.RequestException as e:
        messages.error(request, "Failed to fetch data from the external API.")
        return render(request, 'home.html', {'error': str(e)})

@login_required
def add_to_watchlist(request, movie_id):
    Watchlist.objects.get_or_create(user=request.user, movie_id=movie_id)
    return redirect('home')

@login_required
def remove_from_watchlist(request, movie_id):
    Watchlist.objects.filter(user=request.user, movie_id=movie_id).delete()
    return redirect('home')

def roomPage(request, id):
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    similar_movies_url = f'https://api.themoviedb.org/3/movie/{id}/similar?api_key={api_key}'
    placeholder_image = '/static/Images/placeholders/image_placeholder.png'

    try:
        # Fetch movie data
        response = requests.get(base_url.format(id, api_key))
        data = response.json()
        
        user_score = data.get('vote_average', 0)
        user_score_percentage = user_score * 10

        movie = {
            'id': data.get('id'),
            'title': data.get('title'),
            'overview': data.get('overview'),
            'release_date': data.get('release_date'),
            'poster_url': f"https://image.tmdb.org/t/p/original{data.get('poster_path')}" if data.get('poster_path') else placeholder_image,
            'backdrop_url': f"https://image.tmdb.org/t/p/original{data.get('backdrop_path')}" if data.get('backdrop_path') else placeholder_image,
            'likes': data.get('vote_count'),
            'genres': [genre['name'] for genre in data.get('genres', [])],
            'user_score_percentage': user_score_percentage,
        }

        room, created = Room.objects.get_or_create(
            tmdb_id=movie['id'],
            defaults={
                'title': movie['title'],
                'overview': movie['overview'],
                'release_date': movie['release_date'],
                'poster_url': movie['poster_url'],
                'backdrop_url': movie['backdrop_url'],
                'user_score_percentage': movie['user_score_percentage'],
                'genres': movie['genres'],
            }
        )

        similar_movies_response = requests.get(similar_movies_url)
        similar_movies_data = similar_movies_response.json().get('results', [])[:10]

        similar_movies = [
            {
                'id': sm.get('id'),
                'title': sm.get('title'),
                'poster_url': f"https://image.tmdb.org/t/p/original{sm.get('poster_path')}" if sm.get('poster_path') else placeholder_image
            }
            for sm in similar_movies_data
        ]

        credits_url = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key={api_key}"
        credits_response = requests.get(credits_url)
        credits_data = credits_response.json()

        # Extract cast details
        cast_details = [
            {
                'name': member['name'],
                'character': member['character'],
                'profile_path': f"https://image.tmdb.org/t/p/original{member['profile_path']}" if member['profile_path'] else placeholder_image
            }
            for member in credits_data.get('cast', [])
        ]

        comments = Comment.objects.filter(room=room).order_by('date_created')

        context = {
            'movie': movie,
            'similar_movies': similar_movies,
            'cast_details': cast_details,
            'comments': comments,
            'room': room,
        }

        return render(request, 'room.html', context)
    except requests.RequestException as e:
        messages.error(request, "Failed to fetch data from the external API.")
        return render(request, 'room.html', {'error': str(e)})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, 'Username does not exist')
                return render(request, 'login.html')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is wrong')
        else:
            messages.error(request, 'Username and password are required')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def my_view(request):
    context = {
        'path': request.path,
    }
    return render(request, 'home.html', context)

def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if len(password1) < 8:
                messages.error(request, 'Password must be at least 8 characters long')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def get_movies_by_genre(genre_id):
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = 'https://api.themoviedb.org/3/genre/{}/movies?api_key={}'

    response = requests.get(base_url.format(genre_id, api_key))
    data = response.json()
    return data['results'][:20]

def genrePage(request, genre_id):
    genre_names = {
        10749: 'Romance',
        28: 'Action',
        27: 'Horror',
        9648: 'Mystery',
        16: 'Romance Anime'
    }
    try:
        movies = get_movies_by_genre(genre_id)
        genre_name = genre_names.get(genre_id, 'Unknown Genre')

        context = {
            'genre_name': genre_name,
            'movies': movies
        }
        return render(request, 'genre.html', context)
    except requests.RequestException as e:
        messages.error(request, "Failed to fetch data from the external API.")
        return render(request, 'genre.html', {'error': str(e)})

def celebrity_profile(request, id):
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = f'https://api.themoviedb.org/3/person/{id}?api_key={api_key}'

    try:
        # Fetch celebrity data
        response = requests.get(base_url)
        data = response.json()

        celebrity = {
            'id': data.get('id'),
            'name': data.get('name'),
            'profile_picture_url': f"https://image.tmdb.org/t/p/original{data.get('profile_path')}" if data.get('profile_path') else None,
            'biography': data.get('biography', 'Biography not available.'),
            'birth_date': data.get('birthday'),
            'popularity': data.get('popularity')
        }

        context = {
            'celebrity': celebrity
        }

        return render(request, 'celebrity_profile.html', context)
    except requests.RequestException as e:
        messages.error(request, "Failed to fetch data from the external API.")
        return render(request, 'celebrity_profile.html', {'error': str(e)})

def get_top_movies():
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'
    response = requests.get(base_url.format(api_key))
    data = response.json().get('results', [])[:10]

    top_movies = [
        {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'poster_url': f"https://image.tmdb.org/t/p/original{movie.get('poster_path')}" if movie.get('poster_path') else None,
            'release_date': movie.get('release_date'),
            'likes': movie.get('vote_count')
        }
        for movie in data
    ]

    return top_movies

def get_popular_genres():
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    pexels_api_key = '49S8sYPnL8EJ6Q3vS66MkRg41Ls8cvUCJrJLv2rG5MWdC64JoodbgJRS'
    genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
    response = requests.get(genre_url)
    data = response.json().get('genres', [])[:10]

    top_genre = []
    for genre in data:
        pexels_url = f'https://api.pexels.com/v1/search?query={genre["name"]}&per_page=1'
        pexels_response = requests.get(pexels_url, headers={'Authorization': pexels_api_key})
        pexels_data = pexels_response.json()
        image_url = pexels_data['photos'][0]['src']['medium'] if pexels_data['photos'] else '/static/images/default_genre.jpg'
        
        top_genre.append({
            'id': genre.get('id'),
            'name': genre.get('name'),
            'poster_url': image_url
        })
    
    return top_genre

def format_revenue(revenue):
    if revenue >= 1_000_000:
        return f"${revenue / 1_000_000:.1f}m"
    elif revenue >= 1_000:
        return f"${revenue / 1_000:.1f}k"
    else:
        return str(revenue)

def get_top_box_office_movies():
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    popular_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    response = requests.get(popular_url)
    data = response.json().get('results', [])[:10]

    top_box_office = []
    for movie in data:
        movie_id = movie.get('id')
        details_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        details_response = requests.get(details_url)
        details_data = details_response.json()
        
        revenue = details_data.get('revenue', 0)
        formatted_revenue = format_revenue(revenue)
        
        top_box_office.append({
            'id': movie_id,
            'title': movie.get('title'),
            'revenue': formatted_revenue,
            'poster_url': f"https://image.tmdb.org/t/p/w92{movie.get('poster_path')}" if movie.get('poster_path') else None
        })
    
    return top_box_office

def get_upcoming_movies():
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    upcoming_url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}'
    response = requests.get(upcoming_url)
    data = response.json().get('results', [])[:10]

    upcoming_movies = [
        {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'poster_url': f"https://image.tmdb.org/t/p/w92{movie.get('poster_path')}" if movie.get('poster_path') else None,
            'likes': movie.get('vote_count')
        }
        for movie in data
    ]
    return upcoming_movies

def get_top_news():
    api_key = '2bf99f487550492a8c130951600c971c'
    news_url = f'https://newsapi.org/v2/top-headlines?category=entertainment&apiKey={api_key}'
    response = requests.get(news_url)
    data = response.json().get('articles', [])[:6]

    top_news = [
        {
            'title': article.get('title'),
            'url': article.get('url'),
            'summary': article.get('description'),
            'image_url': article.get('urlToImage') if article.get('urlToImage') else 'static/Images/placeholders/image_placeholder.png'
        }
        for article in data
    ]
    return top_news

def searchMovie(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={q}'
    placeholder_image = '/static/Images/placeholders/image_placeholder.png'

    try:
        response = requests.get(search_url)
        data = response.json().get('results', [])[:10]

        searched_movies = [
            {
                'id': movie.get('id'),
                'title': movie.get('title'),
                'poster_url': f"https://image.tmdb.org/t/p/original{movie.get('poster_path')}" if movie.get('poster_path') else placeholder_image,
                'year_released': movie.get('release_date', '')[:4],  # Extract the year from the release date
                'likes': movie.get('vote_count')
            }
            for movie in data
        ]

        context = {
            'searched_movies': searched_movies,
            'query': q,
        }
        return render(request, 'searchedMovies.html', context)
    except requests.RequestException as e:
        messages.error(request, "Failed to fetch data from the external API.")
        return render(request, 'searchedMovies.html', {'error': str(e), 'query': q})

def getTop50movies(request):
    api_key = '484208b7f5d8c7cfbc90a4b50dab9099'
    base_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key={}&page={}'
    placeholder_image = '/static/Images/placeholders/image_placeholder.png'
    
    all_top_movies = []
    page = 1
    while True:
        response = requests.get(base_url.format(api_key, page))
        data = response.json()
        
        if 'results' not in data or not data['results']:
            break
        
        movies = data['results']
        for movie in movies:
            movie_data = {
                'id': movie.get('id'),
                'title': movie.get('title'),
                'poster_url': f"https://image.tmdb.org/t/p/original{movie.get('poster_path')}" if movie.get('poster_path') else placeholder_image,
                'year_released': movie.get('release_date', '')[:4],
                'rating': movie.get('vote_average'),
                'likes': movie.get('vote_count'),
            }
            all_top_movies.append(movie_data)
        
        if len(all_top_movies) >= 50 or page >= data.get('total_pages', page):
            break
        
        page += 1
    
    context = {
        'top_movies': all_top_movies[:50],
    }
    return render(request, 'top-50-movies.html', context)

