# Tasks
- try out dbc and themes like:
`app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])`
- Try not storing large variables instead since they are naturally global they can be accessed just like normal
- Try client side callbacks (requires writing the function in javascript)
- [App Life Cycle](https://dash.plotly.com/app-lifecycle)
- Get bootstrap 5 style sheet to work:
  -  [bootswatch](https://bootswatch.com/)
  -  [link](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- Time animated graph
- Try bootstrap cards
- Dash table
```
filter_action="native",
sort_action="native",
```


# Dash

### What is it?
Open-source Python repository for data visualization interfaces. It is built by Plotly and was released in 2017. It uses:
- Flask for the web server
- React.js for the user interface
- Plotly to generate charts

### How does it compare to other web frameworks?
- It is not a full scale web framework
- It is more complex than options like Streamlit or Wave that do not require any style code.

### Main App Pieces
- Components
- Callbacks
- Layout
- Style
- Visualization
- Data access/processing

### Dash Components
- Dash core components
- Dash HTML components
- Dash table
- Dash bootstrap components

### Callbacks
- Decorator for the app object
- Input, Output, and State
- Only one callback can send to a given output attribute (dbc workaround)
- Can be used to update the page layout
- Can be used for user login/verification with header info

### Layout


### Style
- Component-level vs CSS-level (Cascading Style Sheets) (different syntax: camelCase vs lower-hyphen-case)
- External vs custom style sheets (bootstrap 5)

#### Style Example
Python:
`html.H1('Test Dash App', style={'textAlign':'center'})`

HTML:
`<h1 style="text-align:center;">Test Dash App</h1>` 

### Plotly visualization
- Plotly graph objects
- Plotly express
- Highlight built in features like selection

### Dash Add-ons
- Dash bootstrap components
- Output to a callback more than once
- [mantine](https://www.dash-mantine-components.com/)

### What is run on start-up versus user loading

### Sources
- [Real Python](https://realpython.com/python-dash/)
- [Building an App](https://medium.com/innovation-res/how-to-build-an-app-using-dash-plotly-and-python-and-deploy-it-to-aws-5d8d2c7bd652)
- [Video Tutorial](https://www.youtube.com/watch?v=7m0Bq1EGPPg)
- [Hello Dash - DBC Guide](https://hellodash.pythonanywhere.com/)
- [Dash Book Project](https://github.com/DashBookProject/Plotly-Dash)
