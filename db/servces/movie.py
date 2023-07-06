from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: int | list[int] | None = None,
        actors_ids: int | list[int] | None = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        movies = Movie.objects.filter(actors__id__in=actors_ids)
        movies.filter(genres__id__in=genres_ids)
        return movies.distinct()

    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()

    return Movie.objects.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    movie.genres.set(genres_ids)
    movie.actors.set(actors_ids)
