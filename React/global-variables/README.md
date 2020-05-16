# Use Case
In one of my React projects, I have used some JS files as data for my app instead of using DB.
usually, you will put these files in ```src/assets/data``` folder, 
then when you execute ```npm run build``` command, all these files will be minified and merge into fewer files.

so what is the problem with that?
---------------------------------
if using these files as my DB, I will need to edit them, and it's not an easy task after merged with other files.

so what can we do?
------------------
putting these files in ```public``` folder will ensure these files will not be processed by webpack. 
Instead, it will be copied into the build folder untouched. (https://create-react-app.dev/docs/using-the-public-folder/)

sounds good, tell me what need to be done.
------------------------------------------
for the example let's assume we have one JS file ```data.js``` in ```src/assets/data``` folder.
this is how this file looks:
```js
const myData = [{'id':1,'name':'A'},{'id':2,'name':'B'}]
export default myData;
```
<br />


1. edit ```data.js``` file:
    ```js
    window.myData = [{'id':1,'name':'A'},{'id':2,'name':'B'}]
    ```

2. move the JS file to ```public``` folder
  
3. in ```public/index.html``` file, add the next line at the end of the ```body``` (just before ```</body>```):
    ```html
      <script src="%PUBLIC_URL%/data.js"></script>
    ```

4. inside any JS code you can simply use the next variable: ```window.myData```

5. that's it! 
