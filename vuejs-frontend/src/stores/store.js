import { ref, reactive, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useStore = defineStore('store', () => {
  const sepalLength = ref(0.0)
  const sepalWidth = ref(0.0)
  const petalLength = ref(0.0)
  const petalWidth = ref(0.0)
  const link = ref('http://127.0.0.1:8000/api/')

  const processRequest = async () => {
    console.log('local: ' + localToken.value)
    const v = {
      sepal_length: sepalLength.value, sepal_width: sepalWidth.value,
      petal_length: petalLength.value, petal_width: petalWidth.value
    }
    const res = await axios.post(link.value, v, {
      headers: {
        Accept: 'application/json',
        //'Content-Type': 'application/json',
        Authorization: `Bearer ${localToken.value}`
      }
    })
    console.log(res.data)
    return res.data
  }

  return { processRequest,  sepalLength, sepalWidth, petalLength, petalWidth}
})
