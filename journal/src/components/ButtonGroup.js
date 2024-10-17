import React from "react";

const ButtonGroup = ({ onSubmit, onClear, loadingSubmit }) => {
  return (
    <div className="button-group">
      <button className="submit-btn" onClick={onSubmit}>
        {loadingSubmit ? "Loading..." : "Submit"}
      </button>
      <button className="clear-btn" onClick={onClear}>
        Clear
      </button>
    </div>
  );
};

export default ButtonGroup;
