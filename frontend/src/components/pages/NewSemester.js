import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { Semesterbo } from '../../api/BusinessObjects';
import ContextErrorMessage from "../dialogs/ContextErrorMessage";


export class NewModuletype extends Component {
    constructor(props) {
        super(props)
    
    

        this.state = {
            id:"",
            name:"",
            title:"",
            
            appError: null,
        
        }
    }


    handleSave = () =>{
        const {setLoading} = this.props
        var Semester = new Semesterbo();
        Semester.setID(this.state.id);
        Semester.setName(this.state.name);
        Semester.setTitle(this.state.title);
      
        setLoading(`saveNewSemester`, true)
        API.getAPI().addSemester(Semester).then(response => {
            setLoading(`saveNewSemester`, false)
            this.props.handleClose()
        }).catch(e => {
            this.setState({
                appError: e
            });
            setLoading(`saveNewSemester`, false)
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
                {appError?<ContextErrorMessage appError={appError} />:null}
          </>
        )
    }
}

export default NewModuletype
