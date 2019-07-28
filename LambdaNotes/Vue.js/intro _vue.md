# Intro to Vue.js
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