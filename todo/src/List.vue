<template>
  <div class="list">
    <AddTask v-if="show === true"/>
    <h3>Incomplete Tasks({{getInCompleteTasks(tasks).length}})</h3>
    <Task v-for="task in getInCompleteTasks(tasks)" :key="task.id" :task="task" />

    <h3>Complete Tasks ({{getCompleteTasks(tasks).length}})</h3>
    <Task v-for="task in getCompleteTasks(tasks)" :key="task.id" :task="task" />
  </div>
</template>

<script>
import Task from "./Task.vue";
import axios from "axios";
import { ref, onBeforeMount } from "vue";
import AddTask from "./AddTask.vue";
import {getInCompleteTasks, getCompleteTasks} from "./utils.js"

export default {
  name: "List",
  props: ["show"],
  components: { Task, AddTask },
  setup() {
    const tasks = ref([]);
    onBeforeMount(() => {
      axios
        .get("http://127.0.0.1:8000/tasks/", {
          auth: {
            username: "debjit",
            password: "1234",
          },
        })
        .then((res) => {
          tasks.value = res.data;
        });
    });
    return {
      tasks,
      getCompleteTasks,
      getInCompleteTasks
    };
  },
};
</script>

<style scoped>
.list {
  height: calc(100% - 54px);
  overflow-y: scroll;
}

h3{
  margin: 20px 16px 10px 16px;
  color: #929292;
}
</style>