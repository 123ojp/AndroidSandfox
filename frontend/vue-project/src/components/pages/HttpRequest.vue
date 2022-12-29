<template>
  
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="6">
        <p>Request</p>
        <pre class="border code-box">{{req}}</pre>
      </b-col>

      <b-col cols="6">
        <p>Response</p>
        <pre class="border code-box">{{res}}</pre>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  props: {
    req: {
      type: String,
      default: null
    },
    res: {
      type: String,
      default: null
    },
  }
}
</script>

<style scoped>
.code-box {
  padding: 10px;
  border-radius: 5px;
}
</style>