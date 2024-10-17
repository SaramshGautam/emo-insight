import React from "react";
import WordCloud from "react-wordcloud";

const EmotionWordCloud = ({ words = [] }) => {
  const options = {
    rotations: 2,
    rotationAngles: [-90, 0],
    fontSizes: [15, 50],
  };

  return (
    <div className="word-cloud">
      <h3>Emotion Word Cloud</h3>
      <WordCloud options={options} words={words} />
    </div>
  );
};

export default EmotionWordCloud;
