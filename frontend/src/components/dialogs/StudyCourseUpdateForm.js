import React, {Component} from 'react';
import ContextErrorMessage from './ContextErrorMessage';
import LoadingProgress from './LoadingProgress';
import API from '../../api/API';
import {ListItem, TableCell, TableRow, Button, Dialog, DialogActions, DialogTitle, DialogContent, Typography, TextField } from "@material-ui/core"
//import StudyCoursebo from '../../api/BusinessObjects/StudyCoursebo';
import {getCurrentDate} from '../../api/utils';

class StudyCourseUpdateForm extends Component {

    constructor(props) {
        super(props);
        let 
        
            id = 0, 
            name = "", 
            creation_date = "",
            engl_titel = "", 
            abschluss= "",
            semester= 0;
           
          
        if (props.studycourses) {

            id = props.studycourses.getID();
            creation_date = props.studycourses.getErstellungszeitpunkt(getCurrentDate());
            name=props.studycourses.getName();
            engl_titel = props.studycourses.getEnglTitel();
            abschluss = props.studycourses.getAbschluss();
            semester = props.studycourses.getSemester()
        }
    
            


        this.state = {
            id: id,
            creation_date: creation_date,
            name: name,
            engl_titel: engl_titel,
            abschluss: abschluss,
            semester: semester,
            studiengangValidationFailed: false
        }
        console.log(props)
        this.baseState = this.state;
        //State speichern falls cancel
        this.handleSubmit = this.handleSubmit.bind(this);
       


    }

    onInputchange(event) {
        this.setState({
          [event.target.name]: event.target.value
        });
    }

    handleClose = () => {
        // Reset the state
        this.setState(this.baseState);
        this.props.onClose(null);
    }

    studyCourseUpdateFormormClosed = studycourses => {
        if (studycourses) {
            const newStudyCourseList = [...this.state.studycourses, studycourses]
            this.setState({
                studycourses: newStudyCourseList,
                showStudyCourseUpdateForm: false,
            });

        } else {
            this.setState({
                showStudyCourseUpdateForm: false,
            });

        }
    }

    handleSubmit(event) {

        event.preventDefault();

        var studycourses = new studycourses
        studycourses.setID(this.state.id)
        studycourses.setErstellungszeitpunkt(getCurrentDate())
        studycourses.setName(this.state.name)
        studycourses.setEnglTitel(this.state.engl_titel)
        studycourses.setAbschluss(this.state.abschluss)
        studycourses.setSemester(this.state.semester)
        

        API.getAPI().updateStudycourse(studycourses).then((studycourses) => {
            //console.log(studiengang)
            this.setState({
                studycourses: studycourses,
                showStudyCOurseUpdateForm: false
            });
            this.handleClose();
            }).catch(e => 
        this.setState({  
            updatingInProgress: false,
            updatingError: e
        })
    );

     
        
    this.props.onClose(this.state);
   }
   
   textFieldValueChange = (event) => {
    const value = event.target.value;

    let error = false;
    if (value.trim().length === 0){
        error = true;
    }
    this.setState({
        [event.target.id]: event.target.value,
        [event.target.id + "ValidationFailed"]: error,
        [event.target.id + "Edited"]: true
    });
}



    numberValueChange = (event) => {
        const value = event.target.value;
        const re = /^[0-9]{1,3}$/;

        let error = false;
        if (value.trim().length === 0) {
            error = true;
        }
        if (re.test(event.target.value) === false){
            error = true;
        }

        this.setState({
            [event.target.id]: event.target.value,
            [event.target.id + 'ValidationFailed']: error,
            [event.target.id + 'Edited']: true
        });
    }
    render() {
        const { classes, show } = this.props
        const { name, nameValidationFailed, engl_titel, engl_titelValidationFailed,
            abschluss, abschlussValidationFailed, semester, semesterValidationFailed} = this.state;
        return (
            show ? 
                <Dialog open={show} onClose={this.handleClose} maxWidth='sm'>
                    <DialogTitle>

                    </DialogTitle>
                <DialogContent>
                    <form  noValidate autoComplete='off' onSubmit={this.handleSubmit}>
                    <TextField autoFocus type='text' required fullWidth margin='normal' id='name'
                            label='Name' variant="outlined"
                            value={name}
                            onChange={this.textFieldValueChange} error={nameValidationFailed}
                            helperText={nameValidationFailed ? 'Bitte geben Sie den Namen an' : ' '}/>
                    <TextField autoFocus type='text' required fullWidth margin='normal' id='engl_titel'
                            label='Engl_titel' variant="outlined"
                            value={engl_titel}
                            onChange={this.textFieldValueChange} error={engl_titelValidationFailed}
                            helperText={engl_titelValidationFailed ? 'Bitte geben Sie einen englischen Titel an' : ' '}/>
                    <TextField autoFocus type='text' required fullWidth margin='normal' id='abschluss'
                            label='Abschluss' variant="outlined"
                            value={abschluss}
                            onChange={this.textFieldValueChange} error={abschlussValidationFailed}
                            helperText={abschlussValidationFailed ? 'Bitte geben Sie eine Abschluss an' : ' '}/>
                    <TextField autoFocus type='number' required fullWidth margin='normal' id='semester'
                            label='semester' variant="outlined"
                            value={semester}
                            onChange={this.numberValueChange} error={semesterValidationFailed}
                            helperText={semesterValidationFailed ? 'Bitte geben Sie ein Semester an' : ' '}/>     

                    </form>
                </DialogContent>
                <DialogActions>
                    <Button onClick={this.handleSubmit} color="primary">
                        Update
                    </Button>

                    <Button onClick={this.handleClose} color="secondary">
                    Abbrechen

                    </Button>
                </DialogActions>
                </Dialog>
                : null
        );
    }

}

/** Component specific styles */
const styles = theme => ({
    root: {
        width: '100%',
    },
    closeButton: {
        position: 'absolute',
        right: theme.spacing(1),
        top: theme.spacing(1),
        color: theme.palette.grey[500],
    },
    max_teilnehmer: {
        width: 250,
        marginRight: theme.spacing(2)
    },
    formControl: {
        minWidth: 170,
        marginBottom: theme.spacing(1),
    },
    formControlpa: {
        minWidth: 240,
        marginBottom: theme.spacing(1),
        marginLeft: theme.spacing(3)
    },
    formControlmo: {
        width: 435,
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
    },
    radio: {
        marginTop: theme.spacing(2)
    },
    chips: {
        display: 'flex',
        flexWrap: 'wrap'
    },
    chip: {
        margin: 2
    }
});


export default StudyCourseUpdateForm;