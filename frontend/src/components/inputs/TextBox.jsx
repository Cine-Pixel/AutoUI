import { TextField } from "@mui/material";
import PropTypes from "prop-types";

const TextBox = ({ lines, label, placeholder }) => (
  <TextField
    fullWidth
    size="small"
    rows={lines}
    label={label}
    placeholder={placeholder}
  />
);

TextBox.propTypes = {
  lines: PropTypes.number,
  label: PropTypes.string,
  placeholder: PropTypes.string,
};

TextBox.defaultProps = {
  lines: 1,
  label: "",
  placeholder: "",
};

export default TextBox;
