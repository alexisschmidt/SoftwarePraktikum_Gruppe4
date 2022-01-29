import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { Semesterbo } from '../../api/BusinessObjects';
import ErrorHandler from '../atomic/ErrorHandler';


export class NewModuletype extends Component {
    constructor(props) {
        super(props)
    
        //generate some random id 
        var randomID = 9999+Math.floor(Math.random() * 10000);
        /* var date= new Date().toISOString().slice(0, -5); */

        this.state = {
            Semester:[],
            id:randomID,
            hash:"",
            name:"",
            title:"",
            /* aenderungs_datum: date,
            letzte_aenderung_person: "", */
           /*  deprecates: null,
            deprecated: false, */
            appError: null,
        
        }
    }


    handleSave = () =>{
        const {setLoading} = this.props
        var Semester = new Semesterbo();
        Semester.setID(this.state.id);
        Semester.setHash(this.state.hash);
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
    /* handleClick = (pa) => {
        this.setState({
            id:pa.id,
            hash:pa.hash,
            name:pa.name,
            titel_englisch:pa.titel_englisch,
            aenderungs_datum: pa.aenderungs_datum,
            letzte_aenderung_person: pa.letzte_aenderung_person,
        })
    } */

    render() {
        const {name, title, appError, semester} = this.state;
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

<TextField onChange={(event)=>this.setState({semester:event.target.value})}
                  autoFocus
                  margin="dense"
                  id="semester"
                  label="Semester"
                  type="text"
                  fullWidth
                  variant="standard"
                  value={semester}
                />
               
                <Button variant="contained" color="primary" onClick={this.handleSave}> Speichern </Button>
                {appError?<ErrorHandler appError={appError} />:null}
          </>
        )
    }
}

export default NewModuletype
