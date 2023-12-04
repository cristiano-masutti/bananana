<template>
  <div style="background-color: #242424; height: 75vh; overflow-y: auto;">
    <div class="album-container">
      <AlbumRecord v-for="(result, index) in results" :key="result.artist" :result="result" :isLastItemOnLeft="isLastItemOnLeft(index)" />
    </div>
  </div>
</template>

<script>
import AlbumRecord from './AlbumRecord.vue'

export default {
  name: 'SharkVue',
  components: {
    AlbumRecord
  },
  props: {
    results: []
  },
  data() {
    return {
      msg: ""
    }
  },
  methods: {
    isLastItemOnLeft(index) {
      // Check if the current item is the last one and if it's an odd index
      return index === this.results.length - 1 && this.results.length % 2 !== 0;
    }
  }
}
</script>

<style scoped>
.album-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* Align items to the start (left) */
}

/* Adjust the width of AlbumRecord components as needed */
.album-container AlbumRecord {
  width: 48%; /* Adjust the width as per your layout */
  margin-bottom: 10px; /* Add margin for spacing between elements */
}

.album-container AlbumRecord:last-child {
  margin-right: 0; /* Remove right margin for the last item */
}

.album-container AlbumRecord:last-child.left {
  margin-right: auto; /* Move the last item to the left by using auto margin */
}
</style>
