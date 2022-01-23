import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
   Button, IconButton, Dialog, DialogContent, DialogContentText,
    DialogTitle, DialogActions, TextField
} from '@mui/material';
import CloseIcon from '@material-ui/icons/Close';
import ContextErrorMessage from './ContextErrorMessage';
import LoadingProgress from './LoadingProgress';

import Spobo from '../../api/BusinessObjects/Spobo';
import API from '../../api/API';


class SpoForm extends Component {

    constructor(props) {
        super(props);
        this.state = {

            id: null,

            name: '',
            nameValidationFailed: false,
            nameEdited: false,

            title: null,
            titleValidationFailed: false,
            titleEdited: false,

            start_semester: null,
            start_semesterValidationFailed: false,
            start_semesterEdited: false,

            end_semester: null,
            end_semesterValidationFailed: false,
            end_semesterEdited: false,
            
            studyCourse: null,
            studyCourseValidationFailed: false,
            studyCourseEdited: false,

            //wurde importiert aus der Main

            addingError: null,
            addingInProgress: false,

            updatingError: null,
            updatingInProgress: false
        };
        this.baseState = this.state;
    }

    addSpo = () => {
        let newSpo = new Spobo()
        newSpo.setID(0)
        newSpo.setName(this.state.name)
        newSpo.setTitle(this.state.title)
        newSpo.setStart_semester(this.state.start_semester)
        newSpo.setEnd_semester(this.state.end_semester)
        newSpo.setStudycourse(this.state.studycourse)

       
        API.getAPI().addSpo(newSpo).then(spo => {
           
            this.setState(this.baseState);
            this.props.onClose(spo); //Aufrufen parent in backend
        }).catch(e =>
            this.setState({
                addingInProgress: false,
                addingError: e
            })
        );
        // Ladeanimation einblenden
        this.setState({
            addingProgress: true,
            addingError: null
        });
    }

    // Validierung der Textfeldaenderungen 
    textFieldValueChange = (event) => {
        const value = event.target.value;

        let error = false;
        if (value.trim().length === 0) {
            error = true;
        }
        this.setState({
            [event.target.id]: event.target.value,
            [event.target.id + 'ValidationFailed']: error,
            [event.target.id + 'Edited']: true
        });
    }

    numberValueChange = (event) => {
        const value = event.target.value;
        const re = /^[0-9]{1,10}$/;

        let error = false;
        if (value.trim().length === 0) {
            error = true;
        }
        if (re.test(event.target.value) === false) {
            error = true;
        }

        this.setState({
            [event.target.id]: event.target.value,
            [event.target.id + 'ValidationFailed']: error,
            [event.target.id + 'Edited']: true
        });
    }

    getInfos = () => {
        if (this.props.spo) {
            const {spo}=this.props
            
        

            this.setState({
                id: spo.id,
                name: spo.name,
                title: spo.title,
                start_semester: spo.start_semester,
                end_semester: spo.end_semester,
                semester: spo.semester,
                studyCourse: spo.studyCourse,
                //anpassen von id?
            })
        }
    }


    handleClose = () => {
        this.setState(this.baseState);
        this.props.onClose(null);
    }



    render() {
        const { show, spo } = this.props;
        const {

            id,
            idValidationFailed,
            idEdited,

            name,
            nameValidationFailed,
            nameEdited,

            title,
            titleValidationFailed,
            titleEdited,

            start_semester,
            start_semesterValidationFailed,
            start_semesterEdited,

            end_semester,
            end_semesterValidationFailed,
            end_semesterEdited,

            studyCourse,
            studyCourseValidationFailed,
            studyCourseEdited,

            //anpassen ID?



            addingInProgress,
            addingError,
            updatingInProgress,
            updatingError, } = this.state;

        let title = '';
        let header = '';

        if (spo) {
            // Projekt objekt true, somit ein edit
            title = `Spo "${spo.name}" erstellen`;
            header = 'Neue Spo Daten einfügen';
        } else {
            title = 'Erstelle eine neue Spo';
            header = 'Spo Daten einfügen';
        }


        return (
            show ?
                <Dialog open={show} onEnter={this.getInfos} onClose={this.handleClose} maxWidth='xs' fullWidth>
                    <DialogTitle>{title}
                        <IconButton onClick={this.handleClose}>
                            <CloseIcon />
                        </IconButton>
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            {header}
                        </DialogContentText>

                        <form noValidate autoComplete='off'>

                        <TextField autoFocus type='text' required fullWidth margin='small' id='id' label='id' variant="outlined" value={id}
                                onChange={this.numberFieldValueChange} error={idValidationFailed} />

                            <TextField autoFocus type='text' required fullWidth margin='small' id='name' label='Sponame' variant="outlined" value={name}
                                onChange={this.textFieldValueChange} error={nameValidationFailed} />

                            <TextField type='text' required fullWidth margin='small' id='title' label='Title' variant="outlined" value={title}
                                onChange={this.textFieldValueChange} error={titleValidationFailed} />

                            <TextField  type='text' required fullWidth margin='small' id='start_semester' label='Start Semester' variant="outlined" value={start_semester}
                                onChange={this.numberValueChange} error={start_semesterValidationFailed} />


                            <TextField  autoFocus type='text' required fullWidth margin='small' id='end_semester' label='End Semester' variant="outlined" value={end_semester}
                                onChange={this.numberValueChange} error={end_semesterValidationFailed} />  


                            <TextField  autoFocus type='text' required fullWidth margin='small' id='studyCourse' label='StudyCourse' variant="outlined" value={studyCourse}
                                onChange={this.textFieldValueChange} error={studyCourseValidationFailed} />

                                

                        </form>
                        <LoadingProgress show={addingInProgress || updatingInProgress} />
                        {
                            // Show error message in dependency of Projektart prop
                            spo ?
                                <ContextErrorMessage error={updatingError} contextErrorMsg={`The Spo ${spo.getID()} could not be updated.`} onReload={this.updateSpo} />
                                :
                                <ContextErrorMessage error={addingError} contextErrorMsg={`The Spo could not be added.`} onReload={this.addSpo} />
                        }
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleClose} color='secondary'>
                            Abbrechen
                        </Button>
                        {
                            // If a Projekt is given, show an update button, else an add button
                            spo ?
                                <Button disabled={idValidationFailed ||nameValidationFailed || titleValidationFailed || start_semesterValidationFailed || end_semesterValidationFailed || studyCourseValidationFailed  } variant='contained' onClick={this.updateSpo} color='primary'>
                                    Speichern  
                                    //anpassen 
                        </Button>
                                :
                                <Button disabled={idValidationFailed || !idEdited ||nameValidationFailed || !nameEdited || titleValidationFailed || !titleEdited || start_semesterValidationFailed || !start_semesterEdited || end_semesterValidationFailed || !end_semesterEdited || studyCourseValidationFailed || !studyCourseEdited}
                                    variant='contained' onClick={this.addSpo} color='primary'>
                                    Hinzufügen
                        </Button>
                        }
                    </DialogActions>
                </Dialog>
                : null
        );
    }
}


/** PropTypes */
SpoForm.propTypes = {
    
   
    /** If true, the form is rendered */
    show: PropTypes.bool.isRequired,
    /**  
     * Handler function which is called, when the dialog is closed.
     * Sends the edited or created projektBO's as parameter or null, if cancel was pressed.
     *  
     * Signature: onClose(ProjektBO's projekt);
     */
    onClose: PropTypes.func.isRequired,
}

export default SpoForm;