// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-primevue',
    "nuxt-plotly"
  ],
  primevue: {
    options: {
      ripple: true
    },
    components: {
      include: ['Calendar']
    }
  },
  vite: {    optimizeDeps: {      include: ["plotly.js-dist-min"],    },  },
  css: ['primevue/resources/themes/lara-light-teal/theme.css']
})
