import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { StudyCoursebo } from '../../api/BusinessObjects';
import ContextErrorMessage from "../dialogs/ContextErrorMessage";


export class NewStudyCourse extends Component {
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
        const {setLoading} = this.props
        var StudyCourse = new StudyCoursebo();
        StudyCourse.setID(this.state.id);
        StudyCourse.setName(this.state.name);
        StudyCourse.setTitle(this.state.title);
      
        setLoading(`saveNewStudyCourse`, true)
        API.getAPI().addStudyCourse(StudyCourse).then(response => {
            setLoading(`saveNewStudyCourse`, false)
            this.props.handleClose()
        }).catch(e => {
            this.setState({
                appError: e
            });
            setLoading(`saveNewStudyCourse`, false)
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

export default NewStudyCourse
