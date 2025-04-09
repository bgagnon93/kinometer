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
      sortedMovies: [],
      randomMoviePath: '',
      movieBackdropFile: '',
      movieLogoFile: '',
      moviePosterFile: '',
      score1: '',
      score2: '',
      logoKey: 0, // A key to force re-render the logo animation
      isReady: false, // Flag to check if the images are loaded
      remainingMovies: [], // Track movies not yet shown
      sortBy: 'random', // Default sort method
      sortOrder: 'desc', // Default sort order
    }
  },
  methods: {
    // Sort movies based on endpoint and query parameter
    sortMovies() {
      // Clone the movies array to avoid modifying the original
      let sortedList = [...this.movies];
      
      // Apply sorting based on sortBy
      switch (this.sortBy) {
        case 'jw': // Sort by score1
          sortedList.sort((a, b) => {
            // Handle non-numeric scores
            const scoreA = parseFloat(a.score1) || 0;
            const scoreB = parseFloat(b.score1) || 0;
            return this.sortOrder === 'asc' ? scoreA - scoreB : scoreB - scoreA;
          });
          break;
        case 'bg': // Sort by score2
          sortedList.sort((a, b) => {
            // Handle non-numeric scores
            const scoreA = parseFloat(a.score2) || 0;
            const scoreB = parseFloat(b.score2) || 0;
            return this.sortOrder === 'asc' ? scoreA - scoreB : scoreB - scoreA;
          });
          break;
        case 'title': // Sort by title
          sortedList.sort((a, b) => {
            return this.sortOrder === 'asc' 
              ? a.title.localeCompare(b.title) 
              : b.title.localeCompare(a.title);
          });
          break;
        case 'year': // Sort by releaseYear
          sortedList.sort((a, b) => {
            return this.sortOrder === 'asc' 
              ? a.releaseYear - b.releaseYear 
              : b.releaseYear - a.releaseYear;
          });
          break;
        default: // Random sort (shuffle)
          // No sorting needed for random mode, we'll handle this in updateRandomMovie
          break;
      }
      
      this.sortedMovies = sortedList;
      
      // Reset the remaining movies with the newly sorted list
      this.remainingMovies = [...this.sortedMovies];
    },
    
    updateRandomMovie() {
      // If remainingMovies is empty, reset with sorted movies
      if (this.remainingMovies.length === 0) {
        // For random mode, use the original unsorted movies
        if (this.sortBy === 'random') {
          this.remainingMovies = [...this.movies];
        } else {
          this.remainingMovies = [...this.sortedMovies];
        }
      }
      
      let randomMovie;
      
      if (this.sortBy === 'random') {
        // Get random movie from remaining movies
        const randomIndex = Math.floor(Math.random() * this.remainingMovies.length);
        randomMovie = this.remainingMovies[randomIndex];
        
        // Remove selected movie from remaining list
        this.remainingMovies.splice(randomIndex, 1);
      } else {
        // For sorted modes, take the first movie from the sorted list
        randomMovie = this.remainingMovies.shift();
      }
      
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
    // Get the current path to determine sort method
    const path = window.location.pathname;
    // Extract endpoint - remove leading slash and use the first segment
    const endpoint = path.substring(1).split('/')[0];
    
    // Set sort mode based on endpoint
    if (endpoint === 'bg') {
      this.sortBy = 'bg';
    } else if (endpoint === 'jw') {
      this.sortBy = 'jw';
    } else if (endpoint === 'title') {
      this.sortBy = 'title';
    } else if (endpoint === 'year') {
      this.sortBy = 'year';
    } else {
      this.sortBy = 'random';
    }
    
    // Check for sort order in query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const order = urlParams.get('order');
    if (order === 'asc') {
      this.sortOrder = 'asc';
    } else {
      this.sortOrder = 'desc';
    }
    
    // Sort movies based on the endpoint
    this.sortMovies();
    
    // Initialize remaining movies based on sort method
    if (this.sortBy === 'random') {
      this.remainingMovies = [...this.movies];
    } else {
      this.remainingMovies = [...this.sortedMovies];
    }
    
    // Start displaying movies
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