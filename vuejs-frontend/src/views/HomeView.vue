<script setup>
import FormResult from '../components/FormResult.vue'
import { useStore } from '@/stores/store'
import { storeToRefs } from 'pinia'
const store = useStore()
const { processRequest } = storeToRefs(store)
</script>

<template>
  <main>
    <FormResult />
  </main>
</template>
