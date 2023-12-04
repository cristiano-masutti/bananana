<template>
  <div class="history-container">
    <div class="title">
      <h1 style="color: #f5f5f5;">History</h1>
    </div>
    <div class="history">
      <div v-for="(item, index) in query" :key="index" class="history-item" @click="sendItemToParent(item)">
        {{ item }}
      </div>
    </div>
    <div class="button">
      <button @click="clearHistory" class="clear-button">Clear History</button>
    </div>
  </div>
</template>

<style scoped>
.history-container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 0.3fr 2fr 0.2fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  border-radius: 40px;
  border: 1px solid #f5f5f5;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 10px;
  margin-right: 50px;
  margin-bottom: 30px;
  padding: 15px;
  height: 70vh;
}

h1 {
  margin-left: 10px;
  color: #333;
}

.title {
  display: flex;
  justify-content: center;
  align-items: center;
}

.button {
  display: flex;
  justify-content: center;
  align-items: center;
}

.clear-button {
  grid-column: 1; /* Align to the start of the grid */
  cursor: pointer;
  
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  margin-top: 10px;
  background-color: #242424;
  color: #f5f5f5;
}

.clear-button:hover {
  background-color: #ffe135;
  color: #000;
}

.history {
  overflow-y: auto;
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
</style>
  <script>

  /* eslint-disable */

  export default {
    name: 'History',
    props: {
      query: Array,
    },
    methods: {
      sendItemToParent(item) {
        this.$emit('item-clicked', item);
      },
      clearHistory() {
        this.$emit('clear-history');
      },
    },
  };
  </script>
  