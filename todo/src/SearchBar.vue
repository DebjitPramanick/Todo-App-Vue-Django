<template>
  <div class="search-bar">
    <input
      type="text"
      placeholder="Search task by name"
      @input="$emit('search', $event.target.value)"
    />
  </div>
</template>

<script>
export default {
  name: "SearchBar",
};
</script>

<style scoped>
.search-bar{
    padding: 16px;
    display: flex;
    justify-content: flex-end;
}
input {
  padding: 8px 10px;
  font-size: 16px;
  outline: 0;
  border: 1px solid black;
  border-radius: 4px;
}
</style>