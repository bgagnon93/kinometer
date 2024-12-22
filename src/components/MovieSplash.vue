<template>
  <div class="splash-container">
    <transition name="fade" mode="default">
      <img 
        id="backdrop"
        alt="Movie Backdrop"
        v-if="isReady" 
        :key="moviePath" 
        :src="'/assets/movies/' + moviePath + '/backdrops/' + backdropPath"
        class="backdrop"
      >
    </transition>
    <transition name="fade" mode="default">
      <img 
        id="logo"
        alt="Movie Logo"
        v-if="isReady"
        :key="logoKey"
        :src="'/assets/movies/' + moviePath + '/logos/' + logoPath"
        class="shift-right"
      >
    </transition>
    <transition name="fade" mode="default">
      <div class="score-container">
        <h1 id="score1" :class="['score', 'shift-right']" v-if="isReady" :key="logoKey">{{ score1 }}</h1>
      </div>
    </transition>
    <transition name="fade" mode="default">
      <div class="score-container">
        <h1 id="score2" :class="['score', 'shift-right']" v-if="isReady" :key="logoKey">{{ score2 }}</h1>
      </div>
    </transition>
  </div>
</template>
  
<script>
  export default {
    name: 'MovieSplash',
    props: {
      moviePath: String,
      backdropPath: String,
      logoPath: String,
      logoKey: Number,
      score1: String, 
      score2: String,
      isReady: Boolean
    }
  }
</script>

<style scoped>
  .splash-container {
    position: relative;
    width: 100%;
    height: 100%;

  }

  .score-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: calc(900vw/16);
  }
  
  #backdrop {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: auto;
    object-fit: cover;
    animation: fade 5s ease-in-out infinite;
  }

  #logo {
    top: 50%;
    left: 50%;
    width: 30%;
    height: auto;
    max-height: 30%;
    object-fit: contain;
    filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.5));
  }

  #score1 {
    color: #DC143C;
    top: 25%;
    left: 25%;
  }

  #score2 {
    color: #32CD32;
    top: 75%;
    left: 75%;
  }

  .shift-right {
    position: absolute;
    margin: 0px;
    transform: translate(-50%, -50%);
    animation: shiftRight 10s linear infinite;
  }

  .score {
    font-size: 10vw;
    font-family: Arial, sans-serif;
    font-weight: bold;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
  }

  /* The transition effect for the fade */
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease, filter 0.5s ease;
  }

  .fade-enter-from, .fade-leave-to {
    opacity: 0;
    filter: blur(10px);
  }

  .fade-enter-to, .fade-leave {
    opacity: 1;
    filter: blur(0);
  }

  @keyframes shiftRight {
    0% {
      transform: translate(-50%, -50%) translateX(-4%); /* Start off-center */
    }
    100% {
      transform: translate(-50%, -50%) translateX(4%); /* Move right */
    }
  }
</style>
  