import { createMuiTheme } from '@material-ui/core/styles';
import { colors } from '@material-ui/core';

const blue = '#9fc3e6';
const black = '#000000';

// Ein benutzerdefiniertes Thema für diese App
const theme = createMuiTheme({
  palette: {
    black,
    blue,
    primary: {
      contrastText: blue,
      dark: colors.indigo[900],
      main: colors.indigo[500],
      light: colors.indigo[100]
    },
    secondary: {
      contrastText: blue,
      dark: colors.blue[900],
      main: colors.blue['A400'],
      light: colors.blue['A400']
    },
    success: {
      contrastText: blue,
      dark: colors.green[900],
      main: colors.green[600],
      light: colors.green[400]
    },
    info: {
      contrastText: blue,
      dark: colors.blue[900],
      main: colors.blue[600],
      light: colors.blue[400]
    },
    warning: {
      contrastText: blue,
      dark: colors.orange[900],
      main: colors.orange[600],
      light: colors.orange[400]
    },
    error: {
      contrastText: blue,
      dark: colors.red[900],
      main: colors.red[600],
      light: colors.red[400]
    },
    text: {
      primary: colors.blueGrey[800],
      secondary: colors.blueGrey[600],
      link: colors.blue[600]
    },
    background: {
      default: '#F4F6F8',
      paper: blue
    },
    icon: colors.blueGrey[600],
    divider: colors.grey[200]
  }, 
});



export default theme;