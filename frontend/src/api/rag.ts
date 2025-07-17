// Add the following for Vite environment variable typing
interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "/ask";

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
