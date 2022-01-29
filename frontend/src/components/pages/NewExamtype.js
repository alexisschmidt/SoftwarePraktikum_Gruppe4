import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { ExamTypebo } from '../../api/BusinessObjects' 
import ContextErrorMessage from "../dialogs/ContextErrorMessage";


export class NewExamtype extends Component {
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
        var ExamType = new ExamTypebo();
        ExamType.setID(this.state.id);
        ExamType.setName(this.state.name);
        ExamType.setTitle(this.state.title);
      
        setLoading(`saveNewExamtype`, true)
        API.getAPI().addExamtype(ExamType).then(response => {
            setLoading(`saveNewExamtype`, false)
            this.props.handleClose()
        }).catch(e => {
            this.setState({
                appError: e
            });
            setLoading(`saveNewExamtype`, false)
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

export default NewExamtype
