import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import Semesterbo from '../../api/BusinessObjects/Semesterbo';
import ContextErrorMessage from "../dialogs/ContextErrorMessage";


export class NewSemester extends Component {
    constructor(props) {
        super(props)
    
    

        this.state = {
            id:null,
            name:null,
            title:null,
            
            appError: null,
        
        }
    }


    handleSave = () =>{
        var semester = new Semesterbo();
        semester.setID(this.state.id);
        semester.setName(this.state.name);
        semester.setTitle(this.state.title);
      
        
        API.getAPI().addSemester(semester).then(response => {
            this.props.handleClose()
        }).catch(e => {
            this.setState({
                appError: e
            });
        });
        
        
    }
   
    render() {
        const {name, title, appError,} = this.state;
        return (
            <>
               
                <TextField onChange={(event)=>this.setState({name:event.target.value})}
                    autoFocus
                    margin="dense"
                    id="name"
                    label="Name"
                    type="text"
                    fullWidth
                    variant="standard"
                    value={name}
                />
                <TextField onChange={(event)=>this.setState({title:event.target.value})}
                  autoFocus
                  margin="dense"
                  id="name"
                  label="Englischer Titel"
                  type="text"
                  fullWidth
                  variant="standard"
                  value={title}
                />


               
                <Button variant="contained" color="primary" onClick={this.handleSave}> Speichern </Button>
                <ContextErrorMessage 
                error={appError}
                contextErrorMsg={'Das Semester kann nicht hinzugefügt werden'}
                onReload={this.handleSave}
                />
          </>
        )
    }
}

export default NewSemester
