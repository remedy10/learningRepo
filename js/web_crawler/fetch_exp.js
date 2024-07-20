async function logMovies() {
  try {
    const response = await fetch("https://wagslane.dev");
    console.log(response.status);
    if (response.status >= 400) {
      console.log("ok");
    }
    const movies = await response.text();
    /*
    API'ler Json döndüğü için response.json() yaparız ama bu normal site
    olduğu için html döner o yüzden response.text() yaparız.
    bunu zaten response.header.contentType ile anlayabilirsin.
    */
    console.log(movies);
  } catch (error) {
    console.log(error.message);
  }
}
logMovies();
