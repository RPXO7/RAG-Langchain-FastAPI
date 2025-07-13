import axios from "axios";

const API_URL = "http://127.0.0.1:8000/ask";

export interface AskResponse {
  question: string;
  answer: string;
  sources: string[];
}

export default async function askQuestion(query: string): Promise<AskResponse> {
  try {
    const response = await axios.post<AskResponse>(API_URL, { query });
    return response.data;
  } catch (error) {
    console.error("Error asking question:", error);
    return {
      question: query,
      answer: "⚠️ Something went wrong. Please try again.",
      sources: [],
    };
  }
}
