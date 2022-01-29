import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { ExamTypeBO } from '../../api/BusinessObjects';
import ErrorHandler from '../atomic/ErrorHandler';


export class NewExamtype extends Component {
    constructor(props) {
        super(props)
    
        //generate some random id 
        var randomID = 9999+Math.floor(Math.random() * 10000);
        /* var date= new Date().toISOString().slice(0, -5); */

        this.state = {
            ExamType:[],
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
        var ExamType = new ExamTypeBO();
        ExamType.setID(this.state.id);
        ExamType.setHash(this.state.hash);
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
        const {name, title, appError, examtype} = this.state;
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

<TextField onChange={(event)=>this.setState({examtype:event.target.value})}
                  autoFocus
                  margin="dense"
                  id="examtype"
                  label="Prüfungsart"
                  type="text"
                  fullWidth
                  variant="standard"
                  value={examtype}
                />
               
                <Button variant="contained" color="primary" onClick={this.handleSave}> Speichern </Button>
                {appError?<ErrorHandler appError={appError} />:null}
          </>
        )
    }
}

export default NewExamtype
