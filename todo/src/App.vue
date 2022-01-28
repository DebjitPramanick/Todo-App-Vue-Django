<template>
  <div class="page">
    <div class="container">
      <div class="header">
        <h3>Daily Todo App</h3>
        <button @click="addNew = !addNew">Add Task</button>
      </div>

      <List :show='addNew'/>
    </div>
  </div>
</template>

<script>
import List from './List.vue';
import {ref} from 'vue'
export default {
  components: { List },
  name: "App",
  setup(){
    const addNew = ref(false)
    console.log(addNew.value)
    return {
      addNew
    }
  }
};
</script>

<style scoped>
* {
  font-family: Arial, Helvetica, sans-serif;
  padding: 0;
  margin: 0;
}

.page{
  display: flex;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 16px);
}
.container {
  height: calc(100vh - 250px);
  width: calc(100vh - 250px);
  box-shadow:  0 0 10px #c0c0c0;
  border-radius: 10px;
  overflow: hidden;
}

.header {
  background: #ff9138;
  color: #fff;
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
button{
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  outline: 0;
  border: 0;
  background: #fff;
}

::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  border-radius: 10px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #dadada; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #858585; 
}
</style>
