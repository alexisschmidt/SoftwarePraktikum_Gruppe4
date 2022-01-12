import { createTheme } from '@mui/material/styles'
import { indigo, blue, red, green, grey, orange, blueGrey } from '@mui/material/colors';


const black = '#000000';

// Ein benutzerdefiniertes Thema für diese App
const theme = createTheme({
  palette: {
    black,
    blue,
    primary: {
      contrastText: blue,
      dark: indigo[900],
      main: indigo[500],
      light:indigo[100]
    },
    secondary: {
      contrastText: blue,
      dark: blue[900],
      main: blue['A400'],
      light: blue['A400']
    },
    success: {
      contrastText: blue,
      dark: green[900],
      main: green[600],
      light: green[400]
    },
    info: {
      contrastText: blue,
      dark: blue[900],
      main: blue[600],
      light: blue[400]
    },
    warning: {
      contrastText: blue,
      dark: orange[900],
      main: orange[600],
      light: orange[400]
    },
    error: {
      contrastText: blue,
      dark: red[900],
      main: red[600],
      light: red[400]
    },
    text: {
      primary: blueGrey[800],
      secondary: blueGrey[600],
      link: blue[600]
    },
    background: {
      default: '#F4F6F8',
      paper: blue
    },
    icon: blueGrey[600],
    divider: grey[200]
  }, 
});



export default theme;