import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
    withStyles, Button, IconButton, Dialog, DialogContent, DialogContentText,
    DialogTitle, DialogActions, TextField
} from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import ContextErrorMessage from './ContextErrorMessage';
import LoadingProgress from './LoadingProgress';

import { ElectivAPI, Modulebo } from '../../api';


class SpoForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            name: '',
            nameValidationFailed: false,
            nameEdited: false,

            ects: null,
            ectsValidationFailed: false,
            ectsEdited: false,

            sws: null,
            swsValidationFailed: false,
            swsEdited: false,

            addingError: null,
            addingInProgress: false,

            updatingError: null,
            updatingInProgress: false
        };
        this.baseState = this.state;
    }

    addModule = () => {
        let newModule = new Modulebo()
        newModule.setID(0)
        newModule.setname(this.state.name)
        newModule.set_ects(this.state.ects)
        newModule.set_sws(this.state.sws)
        newModule.set_modulepart(this.state.modulepart)
        ElectivAPI.getAPI().addModule(newModule).then(module => {
            this.props.getmodule()
            this.setState(this.baseState);
            this.props.onClose(module); //Aufrufen parent in backend
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

    updateModule = () => {
        let module = this.props.module;
        module.setname(this.state.name)
        module.set_ects(this.state.ects)
        module.set_sws(this.state.sws)
        module.set_modulepart(this.state.modulepart)
        ElectivAPI.getAPI().updateProjektart(module).then(module => {
            this.props.getmodule()
            this.setState(this.baseState);
            this.props.onClose(module); //Aufrufen parent in backend
        }).catch(e =>
            this.setState({
                updatingInProgress: false,
                updatingError: e
            })
        );
        // Ladeanimation einblenden
        this.setState({
            updatingInProgress: true,
            updatingError: null
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
        if (this.props.module) {
            let name = this.props.module.getname();
            let ects = this.props.module.get_ects();
            let sws = this.props.module.get_sws();
            let modulepart = this.props.module.get_modulepart();
            this.setState({
                name: name,
                ects: ects,
                sws: sws,
                modulepart: modulepart,
            })
        }
    }


    handleClose = () => {
        this.setState(this.baseState);
        this.props.onClose(null);
    }



    render() {
        const { classes, show, module } = this.props;
        const {
            name,
            nameValidationFailed,
            nameEdited,

            ects,
            ectsValidationFailed,
            ectsEdited,

            sws,
            swsValidationFailed,
            swsEdited,

            /* modulepart,
            modulepartValidationFailed,
            modulepartEdited, */

            addingInProgress,
            addingError,
            updatingInProgress,
            updatingError, } = this.state;

        let title = '';
        let header = '';

        if (module) {
            // Projekt objekt true, somit ein edit
            title = `Module "${module.name}" bearbeiten`;
            header = 'Neue Projektart Daten einfügen';
        } else {
            title = 'Erstelle eine neue Projektart';
            header = 'Projektart Daten einfügen';
        }


        return (
            show ?
                <Dialog open={show} onEnter={this.getInfos} onClose={this.handleClose} maxWidth='xs' fullWidth>
                    <DialogTitle className={classes.dialogtitle}>{title}
                        <IconButton className={classes.closeButton} onClick={this.handleClose}>
                            <CloseIcon />
                        </IconButton>
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            {header}
                        </DialogContentText>

                        <form className={classes.root} noValidate autoComplete='off'>

                            <TextField className={classes.textfield} autoFocus type='text' required fullWidth margin='small' id='name' label='Projektartname' variant="outlined" value={name}
                                onChange={this.textFieldValueChange} error={nameValidationFailed} />

                            <TextField className={classes.textfield} type='text' required fullWidth margin='small' id='ects' label='ECTS' variant="outlined" value={ects}
                                onChange={this.numberValueChange} error={ectsValidationFailed} />

                            <TextField className={classes.textfield} type='text' required fullWidth margin='small' id='sws' label='SWS' variant="outlined" value={sws}
                                onChange={this.numberValueChange} error={swsValidationFailed} />

                        </form>
                        <LoadingProgress show={addingInProgress || updatingInProgress} />
                        {
                            // Show error message in dependency of Projektart prop
                            module ?
                                <ContextErrorMessage error={updatingError} contextErrorMsg={`The Projektart ${module.getID()} could not be updated.`} onReload={this.updateModule} />
                                :
                                <ContextErrorMessage error={addingError} contextErrorMsg={`The Projektart could not be added.`} onReload={this.addModule} />
                        }
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleClose} color='secondary'>
                            Abbrechen
                        </Button>
                        {
                            // If a Projekt is given, show an update button, else an add button
                            module ?
                                <Button disabled={nameValidationFailed || ectsValidationFailed || swsValidationFailed} variant='contained' onClick={this.updateModule} color='primary'>
                                    Speichern
                        </Button>
                                :
                                <Button disabled={nameValidationFailed || !nameEdited || ectsValidationFailed || !ectsEdited || swsValidationFailed || !swsEdited}
                                    variant='contained' onClick={this.addModule} color='primary'>
                                    Hinzufügen
                        </Button>
                        }
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
    textfield: {
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1)
    }
});

/** PropTypes */
SpoForm.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
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

export default withStyles(styles)(SpoForm);