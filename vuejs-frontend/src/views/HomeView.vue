<script setup>
import FormResult from '../components/FormResult.vue'
import { Store } from '@/stores/store'
import { storeToRefs } from 'pinia'
const store = Store()
</script>

<template>
  <main>
    <FormResult @submit-form="store.processRequest" />
  </main>
</template>
