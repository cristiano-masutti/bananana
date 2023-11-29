<template>
    <div style="padding-top:20px;">
        <form class="search-container">
            <input type="text" id="search-bar" placeholder="What can I help you with today?">
            <a href="#"><img class="search-icon" src="http://www.endlessicons.com/wp-content/uploads/2012/12/search-icon.png"></a>
        </form>
    </div>
</template>

<script>


import axios from 'axios'
export default {
    name: 'SharkVue',
    data() {
        return {
            msg: ""
        }
    },
    async mounted() {
        console.log('Component mounted.')
        this.getResponse();
    },
    methods: {
        async getResponse() {
            console.log('Getting response from server.')
            const path = 'http://127.0.0.1:5000/shark';
            await axios.get(path)
                .then((response) => {
                    console.log(response.data);
                    this.msg = response.data;
                })
                .catch(error => {
                    console.log("err", error);
                })
        },
    }

}

</script>

<style>
.search-container{
    width: 100%;
    display: flex;
    flex-direction: row;
    margin: 0 auto;
}
  
input#search-bar{
    margin: 0 auto;
    width: 90%;
    height: 45px;
    padding: 0 20px;
    font-size: 1rem;
    border: 1px solid #D0CFCE;
    outline: none;
    &:focus{
      border: 1px solid #242424;
      transition: 0.35s ease;
      color: #242424;
      &::-webkit-input-placeholder{
        transition: opacity 0.45s ease; 
        opacity: 0;
      }
      &::-moz-placeholder {
        transition: opacity 0.45s ease; 
        opacity: 0;
      }
      &:-ms-placeholder {
        transition: opacity 0.45s ease; 
        opacity: 0;
      }    
    }
}
  
.search-icon{
    background-color: #D0CFCE;
    width: 47px;
    height: 47px;
}
</style>
