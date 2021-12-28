import React from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';


const useStyles = makeStyles(theme => ({
    root: {
      width: '100%',
      marginTop: theme.spacing(2),
      marginBottom: theme.spacing(2),
      padding: theme.spacing(1)
    },
    content: {
      margin: theme.spacing(1),
    }
  }));
  
  function About() {
  
    const classes = useStyles();
  
    return (
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
          <Typography variant='h6'>
            Software Praktikum
          </Typography>
          <br />
          <Typography>
           Programm von Gruppe 4 erstellt <Link href='https://github.com/Theresa17'>Theresa Kottmann</Link> &ensp;,
           <Link href='https://github.com/sr168'>Sarah Rowan</Link>
          </Typography>
          <br />
          <Typography variant='body2'>
            © Copyright 2021, all rights reserved.
          </Typography>
        </div>
      </Paper>
    )
  }
  
  export default About;