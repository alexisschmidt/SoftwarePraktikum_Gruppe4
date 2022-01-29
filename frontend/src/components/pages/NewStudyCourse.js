import React, { Component } from 'react'
import {Button, TextField,} from '@mui/material';
import API from '../../api/API';
import { StudyCoursebo } from '../../api/BusinessObjects';
import ErrorHandler from '../atomic/ErrorHandler';


export class NewStudyCourse extends Component {
    constructor(props) {
        super(props)
    
        //generate some random id 
        var randomID = 9999+Math.floor(Math.random() * 10000);
        /* var date= new Date().toISOString().slice(0, -5); */

        this.state = {
            StudyCourse:[],
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
        var StudyCourse = new StudyCoursebo();
        StudyCourse.setID(this.state.id);
        StudyCourse.setHash(this.state.hash);
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
        const {name, title, appError, studycourse} = this.state;
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

<TextField onChange={(event)=>this.setState({studycourse:event.target.value})}
                  autoFocus
                  margin="dense"
                  id="studycourse"
                  label="Studiengang"
                  type="text"
                  fullWidth
                  variant="standard"
                  value={studycourse}
                />
               
                <Button variant="contained" color="primary" onClick={this.handleSave}> Speichern </Button>
                {appError?<ErrorHandler appError={appError} />:null}
          </>
        )
    }
}

export default NewStudyCourse
