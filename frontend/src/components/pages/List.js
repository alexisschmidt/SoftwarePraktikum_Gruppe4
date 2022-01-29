/* import * as React from 'react';
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import { FixedSizeList } from 'react-window';

function renderRow(props) {
  const { index, style } = props;

  return (
    <ListItem style={style} key={index} component="div" disablePadding>
      <ListItemButton>
        <ListItemText primary={`Item ${index + 1}`} />
      </ListItemButton>
    </ListItem>
  );
}

export default function VirtualizedList() {
  return (
    <Box
      sx={{ width: '100%', height: 400, maxWidth: 360, bgcolor: 'background.paper' }}
    >
      <FixedSizeList
        height={400}
        width={360}
        itemSize={46}
        itemCount={200}
        overscanCount={5}
      >
        {renderRow}
      </FixedSizeList>
    </Box>
  );
} */


/* import { List } from '@material-ui/core';
import React from 'react';   
import ReactDOM from 'react-dom';   
  
const myList = ['Peter', 'Sachin', 'Kevin', 'Dhoni', 'Alisa'];   
const listItems = myList.map((myList)=>{   
    return <li>{myList}</li>;   
});   
ReactDOM.render(   
    <ul> {listItems} </ul>,   
    document.getElementById('app')   
);   
export default List;   */