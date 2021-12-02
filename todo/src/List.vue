<template>
  <div class="list">
    <AddTask v-if="show === true"/>
    <Task v-for="task in tasks" :key="task.id" :task="task" />
  </div>
</template>

<script>
import Task from "./Task.vue";
import axios from "axios";
import { ref, onBeforeMount } from "vue";
import AddTask from "./AddTask.vue";

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
    console.log(tasks.value);
    return {
      tasks,
    };
  },
};
</script>

<style scoped>
.list {
  height: calc(100% - 54px);
  overflow-y: scroll;
}
</style>