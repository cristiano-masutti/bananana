<template>
    <div class="history-container">
      <h1>History</h1>
      <button @click="clearHistory" class="clear-button">Clear History</button>
      <div v-for="(item, index) in query" :key="index" class="history-item" @click="sendItemToParent(item)">
        {{ item }}
      </div>
    </div>
  </template>
  
  <style scoped>
    .history-container {
      background-color: #f5f5f5;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      margin-top: 10px;
      margin-right: 50px;
      margin-bottom: 30px;
      padding: 15px;
      height: 70vh;
      overflow-y: auto;
    }
  
    h1 {
      margin-left: 10px;
      color: #333;
    }
  
    .clear-button {
      cursor: pointer;
      margin-right: 10px;
      background-color: #4285f4;
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 4px;
      transition: background-color 0.3s ease;
    }
  
    .clear-button:hover {
      background-color: #3367d6;
    }
  
    .history-item {
      margin-top: 10px;
      margin-left: 10px;
      padding: 8px;
      cursor: pointer;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 4px;
      transition: background-color 0.3s ease;
    }
  
    .history-item:hover {
      background-color: #f0f0f0;
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
  