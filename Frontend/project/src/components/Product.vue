<template>
  <div class="product">
    <div :style="{ backgroundImage: product.img }" class="back">
      <label>{{ product.cost }} ₿</label>
      <div class="title">
        <h4>{{ product.title }}</h4>
      </div>
    </div>
    <p>{{ product.description }}</p>
    <button @click="buy()">Купить</button>
    <div @click="close()" class="overlay" v-if="open">
      <div class="popup">
        <h4>Отсканируте QR-код для подтверждения покупки</h4>
        <qrcode-code
          class="code"
          :value="value"
          :options="{
            color: {
              dark: '#0074d9',
            },
          }"
        ></qrcode-code>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductComponent",
  props: {
    product: Object,
    user_id: Number,
  },
  methods: {
    buy() {
      var date = new Date();
      this.value = btoa(`{"date": ${date.getDate()}, "user_id": ${this.user_id}, "product_id": ${this.product.id}}`);
      this.open = true;
    },
    close() {
      this.open = false;
    },
  },
  data() {
    return {
      value: [],
      open: false,
    };
  },
};
</script>


<style scoped>
.overlay {
  background-color: rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 0;
  right: 0;
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
}

.popup {
  width: 300px;
  margin: auto;
  padding: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  text-align: center;
  background-color: lightblue;
  border-radius: 10px;
  border: 1px solid lightgrey;
}

.product {
  margin: 10px 5px;
  width: 200px;
  background-color: lightblue;
  border-radius: 10px;
  border: 1px solid lightgrey;
}

.back {
  width: 200px;
  height: 150px;
  background-position: center top;
  background-size: 100%;
  background-repeat: no-repeat;
  border-radius: 10px 10px 0 0;
}

label {
  background-color: lightcoral;
  border: 1px solid red;
  color: white;
  font-size: 15px;
  border-radius: 10px;
  padding: 2px 5px 2px 10px;
  float: right;
  margin: 5px;
}

.title {
  height: inherit;
  display: flex;
  align-items: flex-end;
}

.title h4 {
  font-size: 30px;
  margin: 10px;
}

p {
  margin: 10px;
}

button {
  background-color: #0074d9;
  border: 1px solid blue;
  border-radius: 10px;
  width: 90px;
  height: 30px;
  color: white;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
</style>
