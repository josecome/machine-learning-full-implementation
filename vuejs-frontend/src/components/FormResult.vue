<script setup>
import { reactive } from 'vue'
import { useStore } from '@/stores/store'
import { storeToRefs } from 'pinia'
const store = useStore()
const { sepalLength, sepalWidth, petalLength, petalWidth } = storeToRefs(store)
const data = reactive({ sepal_length: 0.0, sepal_width: 0.0, petal_length: 0.0, petal_width: 0.0,  })
const emit = defineEmits(['submitForm'])
function submit() {
  sepalLength.value = data.sepal_length
  sepalWidth.value = data.sepal_width
  petalLength.value = data.petal_length
  petalWidth.value = data.petal_width
  emit('submitForm')
}
</script>
<template>
  <h1>Home Page</h1>
  <form @submit.prevent>
  <div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">Full Name</span>
  <input type="text" class="form-control" placeholder="Full Name" aria-label="Fullname" aria-describedby="basic-addon1">
</div>
<div>
  <span style="font-size: 12px; color: blue;">Fill with numbers that range from 0.1 to 9.9</span>
</div>
<table>
  <tr>
    <td></td><td><strong>Length</strong></td><td><strong>Width</strong></td>
  </tr>
  <tr>
    <td><strong>Sepal</strong></td>
    <td>
      <input
      type="text"
      class="form-control"
      name="sepal_length"
      id="sepal_length"
      v-model="data.sepal_length"
      aria-describedby="basic-addon1"
      >
    </td>
    <td>
      <input
      type="text"
      class="form-control"
      name="sepal_width"
      id="sepal_width"
      v-model="data.sepal_width"
      aria-describedby="basic-addon1"
      >
    </td>
  </tr>
  <tr>
    <td><strong>Petal</strong></td>
    <td>
      <input
      type="text"
      class="form-control"
      name="petal_length"
      id="petal_length"
      v-model="data.petal_length"
      aria-describedby="basic-addon1"
      >
    </td>
    <td>
      <input
      type="text"
      class="form-control"
      name="petal_width"
      id="petal_width"
      v-model="data.petal_width"
      aria-describedby="basic-addon1"
      >
    </td>
  </tr>
  <tr>
    <td colspan="3">
      <div class="input-group mb-3">
  <label class="input-group-text" for="inputGroupSelect01">Options</label>
  <select class="form-select" id="inputGroupSelect01">
    <option selected>Choose...</option>
    <option value="1">Setosa</option>
    <option value="2">Versicolor</option>
    <option value="3">Virginica</option>
  </select>
</div>
    </td>
  </tr>
  <tr>
    <td colspan="3">
      <button class="btn btn-primary" type="submit">Submit</button>
    </td>
  </tr>
</table>
  </form>
<div id="v"><span>Predicted Value: </span></div>
</template>
<style scoped>
button, #v {
  padding: 6px;
  margin: 6px;
}
span {
  font-size: 28px;
}
</style>
