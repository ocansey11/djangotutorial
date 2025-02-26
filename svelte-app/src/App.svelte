<script>
  import Router from "svelte-spa-router";
  import Signup from "./routes/SignUp.svelte";
  import Login from "./routes/Login.svelte";

  const routes = {
    "/signup": Signup,
    "/login": Login
  };
</script>

<main>
  <Router {routes} />
</main>
