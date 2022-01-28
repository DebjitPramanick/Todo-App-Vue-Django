<template>
  <div class="add">
    <input
      type="text"
      placeholder="Enter task description"
      :value="description.value"
      @change="onChange($event)"
    />
    <button @click="addTask">Add</button>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
export default {
  name: "AddTask",
  setup() {
    const description = ref("");

    const onChange = (e) => {
        console.log(e.target.value)
        description.value = e.target.value
    }

    const addTask = () => {
      axios.post(
        "http://127.0.0.1:8000/tasks/",
        { description: description.value },
        {
          auth: {
            username: "debjit",
            password: "1234",
          },
        }
      ).then(() => {
          window.location.reload()
      })
    };
    return {
      description,
      addTask,
      onChange
    };
  },
};
</script>

<style scoped>
.add {
  display: flex;
  align-items: center;
  padding: 16px;
}

.add input {
  padding: 9px 10px;
  font-size: 16px;
  width: calc(100% - 80px);
  outline: 0;
  border: 1px solid black;
  border-radius: 4px;
  margin-right: 16px;
}

button {
  border-radius: 4px;
  width: 60px;
  padding: 9px 10px;
  font-size: 16px;
  background-image: linear-gradient(45deg, #8163e0, #103e92);
  outline: 0;
  border: 0;
  color: #fff;
  cursor: pointer;
}
</style>