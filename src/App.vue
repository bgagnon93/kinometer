<template>
  <div>
    <div class="app-container splash movie-splash">
      <MovieSplash
        :moviePath="randomMoviePath"
        :backdropPath="movieBackdropFile"
        :logoPath="movieLogoFile"
        :logoKey="logoKey"
        :score1="score1"
        :score2="score2"
        :isReady="isReady"
      />
    </div>
    <div class="app-container splash poster-splash">
      <PosterSplash
        :moviePath="randomMoviePath"
        :posterPath="moviePosterFile"
        :logoKey="logoKey"
        :score1="score1"
        :score2="score2"
        :isReady="isReady"
      />
    </div>
  </div>
</template>

<script>
import MovieSplash from './components/MovieSplash.vue'
import PosterSplash from './components/PosterSplash.vue'
import movies from './data/movies';

export default {
  name: 'App',
  components: {
    MovieSplash,
    PosterSplash
  },
  data() {
    return {
      movies: movies,
      randomMoviePath: '',
      movieBackdropFile: '',
      movieLogoFile: '',
      moviePosterFile: '',
      score1: '',
      score2: '',
      logoKey: 0, // A key to force re-render the logo animation
      isReady: false, // Flag to check if the images are loaded
    }
  },
  methods: {
    updateRandomMovie() {
      const randomMovie = this.movies[Math.floor(Math.random() * this.movies.length)];
      this.randomMoviePath = randomMovie.moviePath;
      this.movieBackdropFile = this.getRandomElement(randomMovie.backdrops);
      this.movieLogoFile = this.getRandomElement(randomMovie.logos);
      this.moviePosterFile = this.getRandomElement(randomMovie.posters);
      this.score1 = randomMovie.score1;
      this.score2 = randomMovie.score2;
      this.preloadImages();
      this.logoKey++;
    },

    // Utility to pick a random element from an array
    getRandomElement(array) {
      return array[Math.floor(Math.random() * array.length)];
    },

    // Preload images before transitioning
    preloadImages() {
      const backdropImg = new Image();
      const logoImg = new Image();
      const posterImg = new Image();
      
      // Set the sources
      backdropImg.src = `/assets/movies/${this.randomMoviePath}/backdrops/${this.movieBackdropFile}`;
      logoImg.src = `/assets/movies/${this.randomMoviePath}/logos/${this.movieLogoFile}`;
      posterImg.src = `/assets/movies/${this.randomMoviePath}/posters/${this.moviePosterFile}`;
      // Wait for both images to load before setting the 'isReady' flag
      Promise.all([
        new Promise(resolve => backdropImg.onload = resolve),
        new Promise(resolve => logoImg.onload = resolve),
        new Promise(resolve => posterImg.onload = resolve),
      ]).then(() => {
        this.isReady = true; // Set ready state to true after loading
      });
    }
  },
  mounted() {
    this.updateRandomMovie();
    setInterval(this.updateRandomMovie, 5000);
  }
}
</script>

<style scoped>
.app-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  background-color: slategrey;
}

.splash {
  display: none; /* Hide all splashes by default */
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* Ensure the image is contained within its parent */
}

.movie-splash {
  display: block; /* Show MovieSplash by default */
}

.poster-splash {
  display: none; /* Hide PosterSplash by default */
}

@media (orientation: portrait) {
  .movie-splash {
    display: none; /* Hide MovieSplash in portrait mode */
  }

  .poster-splash {
    display: block; /* Show PosterSplash in portrait mode */
  }
}
</style>