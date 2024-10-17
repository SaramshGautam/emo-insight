import React from "react";
import ButtonGroup from "./ButtonGroup";

const JournalInput = ({
  journal,
  handleJournalChange,
  handleSubmit,
  handleClear,
  loadingSubmit,
}) => {
  return (
    <div className="left-panel">
      <h2>Your Journal</h2>
      <textarea
        className="journal-input"
        value={journal}
        onChange={handleJournalChange}
        placeholder="Write your thoughts here..."
      />
      <ButtonGroup
        onSubmit={handleSubmit}
        onClear={handleClear}
        loadingSubmit={loadingSubmit}
      />
    </div>
  );
};

export default JournalInput;
