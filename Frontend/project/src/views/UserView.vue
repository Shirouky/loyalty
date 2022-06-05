<template>
  <div>
    <h1>Программа лояльности</h1>
    <div class="profile">
      <div class="user">
        <img :src="user.avatar" />
        <h4>{{ user.username }}</h4>
      </div>
      <label>{{ user.points }} ₿</label>
    </div>
    <h3>Что купить?</h3>
    <div class="products">
      <Product
        v-for="product in products"
        :key="product.id"
        :product="product"
        :user_id="user.id"
      />
    </div>
  </div>
</template>

<script>
import Product from "../components/Product.vue";

export default {
  name: "UserProfile",
  components: {
    Product,
  },
  computed: {
    user(){
      return this.$store.state.user;
    },
    products(){
      return this.$store.state.products;
    }
  },
  created() {
    this.$store.dispatch('SET_USER', 1)
    this.$store.dispatch('SET_PRODUCTS')
  },
  data() {
    return {
      key: 0,
    };
  },
};
</script>


<style scoped>
.products {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.profile {
  display: flex;
  align-items: center;
  justify-content: space-around;
  border-radius: 10px;
  padding: 10px;
  border: 1px solid lightgray;
  margin-bottom: 50px;
}

h1 {
  text-align: center;
}

.user {
  display: flex;
  align-items: center;
  width: 200px;
  justify-content: space-around;
}

h4 {
  font-size: 30px;
  margin: 0;
}

label {
  background-color: lightcoral;
  border: 1px solid red;
  color: white;
  font-size: 15px;
  border-radius: 10px;
  padding: 2px 5px 2px 10px;
  margin: 5px;
}

img {
  display: block;
  width: 50px;
  height: 50px;
  border-radius: 100%;
}
</style>
