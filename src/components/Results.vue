<template>
  <div style="background-color: #242424; height: 75vh; overflow-y: auto; margin-right: 20px">
    <div style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
      <h1 style="color: #fcf8f8;">{{this.sizeResults()}}</h1>
      <div>
        <button class="myButton" v-if="!flagClustering" @click="showClustering">Show Genres</button>
        <button class="myButton" v-else @click="hideClustering">Hide Genres</button>
      </div>
    </div>
    <div v-if="!flagClustering" class="album-container">
      <AlbumRecord v-for="(result, index) in this.datas" :key="result.artist" :result="result" :isLastItemOnLeft="isLastItemOnLeft(index)" />
    </div>
    <div v-else>
        <div v-if="!showAlbums">
        <!-- Display a list of genres -->
        <ul>
          <li class="myButton" style="margin: 10px;" v-for="([genre, albums]) in Array.from(sortedGenresMap)" :key="genre" @click="showAlbumsForGenre(genre)">
            {{ genre }} ({{ albums.length }} albums)
          </li>
        </ul>
      </div>
      <div v-else>
        <AlbumRecord v-for="(result, index) in selectedGenreAlbums" :key="result.artist" :result="result" :isLastItemOnLeft="isLastItemOnLeft(index)" />

        <button class="myButton" @click="showGenres">Back to Genres</button>
      </div>
    </div>
    <button v-if="!flagClustering" class="myButton" style="margin-top: 40px;" @click="loadMore">Load More</button>
  </div>
</template>

<script>
/* eslint-disable */
import { setTransitionHooks } from 'vue';
import AlbumRecord from './AlbumRecord.vue'

export default {
  name: 'Results',
  components: {
    AlbumRecord
  },
  props: {
    results: []
  },
  data() {
    return {
      msg: "",
      flagClustering: false,
      datas: [],
      n: 15,
      sortedGenresMap: new Map(),
      showAlbums: false,
      selectedGenreAlbums: [],
    }
  },
  mounted() {
    this.datas = this.results;
    if (this.results.length > this.n) {
      this.datas = this.results.slice(0, this.n);
    }

    this.clusterMap();
  
  },
  watch: {
    results: function (newResults) {
      this.datas = newResults;
      if (this.results.length > this.n) {
        this.datas = this.results.slice(0, this.n);
      }
      this.n = 15;
      this.flagClustering = false;
      this.clusterMap();
      this.showAlbums = false;
    }
  },
  methods: {
    clusterMap(){
      const genresMap = new Map();

      // Iterate through each result
      this.results.forEach(result => {
        // Check if the result has a "Genres" property
        if (result.Genres) {
          // Split genres string into an array
          const genresArray = result.Genres.split(',');

          // Iterate through genres
          genresArray.forEach(genre => {
            // Trim spaces and convert to lowercase for consistency
            const trimmedGenre = genre.trim().toLowerCase();

            // If the genre doesn't exist in the map, create a new array
            if (!genresMap.has(trimmedGenre)) {
              genresMap.set(trimmedGenre, []);
            }

            // Add the result to the genre array in the map
            genresMap.get(trimmedGenre).push(result);
          });
        }
      });
      const genresArray = Array.from(genresMap);

      // Sort the array based on the length of the genre arrays in descending order
      genresArray.sort((a, b) => b[1].length - a[1].length);

      // Convert the sorted array back to a map
      this.sortedGenresMap = new Map(genresArray);
    },
    loadMore() {
      this.n += 15;
      this.datas = this.results.slice(0, this.n);
    },
    showClustering() {
      this.flagClustering = true;
    },
    hideClustering() {
      this.flagClustering = false;
    },
    isLastItemOnLeft(index) {
      // Check if the current item is the last one and if it's an odd index
      return index === this.results.length - 1 && this.results.length % 2 !== 0;
    },
    sizeResults() {
      let length = this.results.length;
      if (length > 15) {
        return "Returned "+ this.n +" results over " + length + " total.";
      }
      else {
        return "Returned "+ length + " results";
      }
    },
    showAlbumsForGenre(genre) {
      this.selectedGenreAlbums = this.sortedGenresMap.get(genre);

      this.showAlbums = true;
    },
    showGenres() {
      this.showAlbums = false;
    },
  }
}
</script>

<style scoped>

.myButton {
  background-color: #242424;
  border: none;
  color: #f5f5f5;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition: background-color 0.3s ease;
  border-radius: 4px;
  width: 300px;
  margin-right: 40px;
}

ul {
  list-style-type: none;
  padding: 0; /* Remove padding */
  margin: 0; /* Remove margin */
}

.myButton:hover {
  background-color: #ffe135;
  color: #000;
}
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


.history-item {
  margin : 5px;
  padding: 8px;
  cursor: pointer;
  background-color: #242424;
  color: #f5f5f5;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  
}

.history-item:hover {
  background-color: #ffe135;
  color: #000;
}
.cluster-item {
  margin : 5px;
  padding: 8px;
  cursor: pointer;
  background-color: #242424;
  color: #f5f5f5;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  width: 300px;
}

.cluster-item:hover {
  background-color: #ffe135;
  color: #000;
}
</style>
