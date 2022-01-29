import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { ModuleTypebo } from '../../api/BusinessObjects';
import ContextErrorMessage from "../dialogs/ContextErrorMessage";


export class NewModuletype extends Component {
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
        var ModuleType = new ModuleTypebo();
        ModuleType.setID(this.state.id);
        ModuleType.setName(this.state.name);
        ModuleType.setTitle(this.state.title);
      
        setLoading(`saveNewModuletype`, true)
        API.getAPI().addModuletype(ModuleType).then(response => {
            setLoading(`saveNewModuletype`, false)
            this.props.handleClose()
        }).catch(e => {
            this.setState({
                appError: e
            });
            setLoading(`saveNewModuletype`, false)
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
