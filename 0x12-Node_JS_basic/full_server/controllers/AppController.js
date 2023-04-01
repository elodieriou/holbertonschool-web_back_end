class AppController {
  static getHomepage(request, response) {
    return response.send(200, 'Hello Holberton School!');
  }
}
export default AppController;
