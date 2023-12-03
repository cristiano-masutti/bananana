<template>
  <div class="container">
    <div>
      <input v-model="chatInput" @keyup.enter="sendRequest" @focus="onFocus" @focusout="onFocusOut" type="text" class="input" placeholder="Type your message...">
    </div>
    <div class="close-btn" @click="clearInput" :class="{ active: isCloseBtnActive }">&times;</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SharkVue',
  data() {
    return {
      msg: "",
      chatInput: "",
      isCloseBtnActive: false,
      previosQuery: "",
    };
  },
  props: {
    oldQuery: String,
  },
  watch: {
    oldQuery: 'sendRequestOnQueryChange',
  },
  methods: {
    sendRequestOnQueryChange() {
      // Check if oldQuery has a value and send the request immediately
      if (this.oldQuery) {
        this.sendRequestOld();
      }
    },
    sendRequest() {
      console.log('Sending request to server.');
      const path = `http://127.0.0.1:5000/${this.chatInput}`;
      
      axios.get(path)
        .then(response => {
          // Handle the response from the server
          console.log(response.data);
          const data = response.data;
          this.$emit('search', this.chatInput, data);
        })
        .catch(error => {
          // Handle any errors that occurred during the request
          console.error('Error:', error);
        });
        this.previosQuery = "";
    },
    sendRequestOld() {
      this.previosQuery = this.oldQuery;
      const path = `http://127.0.0.1:5000/${this.previosQuery}`;

      axios.get(path)
        .then(response => {
          // Handle the response from the server
          console.log(response.data);
          const data = response.data;
          this.$emit('search', this.chatInput, data);
        })
        .catch(error => {
          // Handle any errors that occurred during the request
          console.error('Error:', error);
        });
    },
    onFocus() {
      this.isCloseBtnActive = true;
    },
    onFocusOut() {
      this.isCloseBtnActive = false;
      this.chatInput = "";
    },
    clearInput() {
      this.chatInput = "";
    },
  }
};
</script>

<style>
.container {
  position: relative;
  padding: 10px 50px;
}

.close-btn {
  position: absolute;
  top: 27px;
  right: 80px;
  font-size: 35px;
  cursor: pointer;
  color: #fff;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.close-btn.active {
  opacity: 1;
  animation: animate 0.5s linear;
}

.input {
  width: 85%;
  border: 1px solid #D9D9D9;
  background: transparent;
  padding: 15px 30px;
  border-radius: 50px;
  outline: none;
  font-size: 18px;
  color: #fff;
  letter-spacing: 1px;
}

::-webkit-input-placeholder {
  color: #fff;
  letter-spacing: 2px;
  text-transform: uppercase;
}

::-moz-placeholder {
  color: #fff;
}

:-ms-input-placeholder {
  color: #fff;
}
</style>
