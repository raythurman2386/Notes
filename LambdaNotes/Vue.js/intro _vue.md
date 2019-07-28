# Intro to Vue.js
# What is Vue
  Vue is a progressive and performant JavaScript framework used for building user interfaces and front end applications
  Vue is one of the most popular JS frameworks available

  The Vue Instance:
    
    var app = new Vue({
      el: '#app', // the element the instance attaches to
      data: {
        product: 'Socks',
        description: 'A warm pair of fuzzy socks.',
      }
    })

    <div class="app">
      <h1>{{ product }}</h1>
      <p>{{ description }}</p>
    </div>

  v-bind - Dynamically binds an attribute to an expression

    v-bind:src = "expression"

    :src="expression" // Shorthand v-bind
    :alt="description"
    :title="toolTip"
    :class="isActive"
    :style="isStyled"
    :disabled="isDisabled"

# Vue CLI
  Great for generating and building Vue apps
  Features include Babel, TypeScript, ESLint, PostCSS
  Includes dev server with hot reload
  Vue UI tool to manage you app in a GUI

    npm install -g @vue/cli

# Vuex
  State management in Vue
  Used to manage app level state similar to redux
  Serves as a central store for all components
  Uses actions to update global state.