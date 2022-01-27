import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import API from "../../api/API";
import ContextErrorMessage from './ContextErrorMessage';
import LoadingProgress from './LoadingProgress';

class StudyCourseDeleteDialog extends Component {

    constructor(props) {
        super(props);

        this.state = {
            deletingInProgress: false,
            deletingError: null
        };
    }

    deleteStudycourse = () => {
        API.getAPI().deleteStudycourse(this.props.studycourses.getID()).then(studycourses => {
        this.setState({
            deletingInProgress: false,              // disable loading indicator
            deletingError: null                     // no error message
          });
          this.props.onClose(this.props.studycourses);  // call the parent with the deleted studiengang
        }).catch(e =>
          this.setState({
            deletingInProgress: false,              // disable loading indicator
            deletingError: e                        // show error message
          })
        );
    
        // set loading to true
        this.setState({
          deletingInProgress: true,                 // show loading indicator
          deletingError: null                       // disable error message
        });
    }

    onClose = () => {
        this.state.show(false)
    }
    
    /** Handles the close / cancel button click event */
    handleClose = () => {
        // console.log(event);
        this.props.onClose(null);
        
    }

    render() {
        const { classes, studycourses, show } = this.props;
        const { deletingInProgress, deletingError } = this.state;

        return (
            show ? 
                <Dialog open={show} onClose={this.handleClose}>
                    <DialogTitle id='delete-dialog-title'>Delete Studiengang
                        <IconButton className={classes.closeButton} onClick={this.handleClose}>
                            <CloseIcon />
                        </IconButton>
                    </DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            Sicher, dass Sie Studiengang(ID: {studycourses.getID()})?
                        </DialogContentText>
                        <LoadingProgress show={deletingInProgress} />
                        <ContextErrorMessage error={deletingError} contextErrorMsg={`The studiengang (ID: ${studycourses.getID()}) could not be deleted.`}
                            onReload={this.deleteStudycourse} />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleClose} color='secondary'>
                            Cancel
                        </Button>
                        <Button variant='contained' onClick={this.deleteStudycourse} color='primary'>
                            Delete
                        </Button>
                    </DialogActions>
                </Dialog>
            : null

        );
    }
}
/** Component specific styles */
const styles = theme => ({
    closeButton: {
      position: 'absolute',
      right: theme.spacing(1),
      top: theme.spacing(1),
      color: theme.palette.grey[500],
    }
});

  /** PropTypes */
  StudyCourseDeleteDialog.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** The CustomerBO to be deleted */
    studycourses: PropTypes.object.isRequired,
    /** If true, the dialog is rendered */
    show: PropTypes.bool.isRequired,
    /**
     * Handler function which is called, when the dialog is closed.
     * Sends the deleted CustomerBO as parameter or null, if cancel was pressed.
     *
     * Signature: onClose(CustomerBO customer);
     */
    onClose: PropTypes.func.isRequired,
}

export default withStyles(styles)(StudyCourseDeleteDialog);